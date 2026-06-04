import os
import subprocess
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class FuzzEngine:
    def __init__(self, workspace: str):
        self.workspace = workspace
        self.has_foundry = self._check_for_foundry()

    def _check_for_foundry(self) -> bool:
        return os.path.exists(os.path.join(self.workspace, "foundry.toml"))

    def run_fuzz_tests(self) -> Dict[str, Any]:
        if not self.has_foundry:
            logger.info("No foundry.toml found. Skipping Fuzz testing.")
            return {"status": "skipped", "reason": "No foundry.toml"}

        logger.info("Foundry project detected. Running Fuzz tests via 'forge test'...")
        
        try:
            # We run forge test with JSON output
            result = subprocess.run(
                ["forge", "test", "--json"],
                cwd=self.workspace,
                capture_output=True,
                text=True,
                timeout=300 # 5 minutes max
            )
            
            output = result.stdout
            
            # Simple parse to see if there are failing tests
            if result.returncode == 0:
                logger.info("Fuzz testing passed successfully.")
                return {"status": "success", "failed_tests": 0, "details": "All Foundry tests passed."}
            else:
                logger.warning("Fuzz testing found failures!")
                # Extract basic failure info (in a real scenario we'd parse the JSON fully)
                return {
                    "status": "failed",
                    "failed_tests": output.count('"status":"Failure"'), # Rough estimate
                    "details": "Foundry tests failed. Check logs for details."
                }
                
        except subprocess.TimeoutExpired:
            logger.error("Fuzz testing timed out.")
            return {"status": "error", "reason": "Timeout exceeded (300s)"}
        except Exception as e:
            logger.error(f"Error running forge: {e}")
            return {"status": "error", "reason": str(e)}
