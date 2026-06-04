import pytest
import os
import sys
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestScannerImports:
    """Verify all core modules can be imported without errors."""

    def test_security_scanner_import(self):
        import security_scanner
        assert hasattr(security_scanner, 'scan_contract')

    def test_vulnerability_validator_import(self):
        import vulnerability_validator
        assert hasattr(vulnerability_validator, 'VulnerabilityValidator')

    def test_gas_optimizer_import(self):
        from gas_optimizer import GasOptimizer
        assert GasOptimizer is not None

    def test_github_commenter_import(self):
        from github_commenter import GitHubCommenter
        assert GitHubCommenter is not None

    def test_fuzz_engine_import(self):
        from fuzz_engine import FuzzEngine
        assert FuzzEngine is not None

    def test_solana_scanner_import(self):
        from solana_scanner import SolanaScanner
        assert SolanaScanner is not None


class TestGasOptimizer:
    """Test the gas optimization detection engine."""

    def setup_method(self):
        self.optimizer_dir = os.path.join(os.path.dirname(__file__), "fixtures")
        os.makedirs(self.optimizer_dir, exist_ok=True)

    def test_detects_uncached_array_length(self):
        test_file = os.path.join(self.optimizer_dir, "test_gas.sol")
        with open(test_file, "w") as f:
            f.write("for (uint i = 0; i < arr.length; i++) {\n")
        from gas_optimizer import GasOptimizer
        opt = GasOptimizer(self.optimizer_dir)
        result = opt.optimize_contract(test_file)
        assert result["status"] == "success"
        assert result["findings_count"] >= 1
        assert any("Uncached Array Length" in f["issue"] for f in result["findings"])

    def test_detects_post_increment(self):
        test_file = os.path.join(self.optimizer_dir, "test_gas2.sol")
        with open(test_file, "w") as f:
            f.write("for (uint i = 0; i < 10; i++)\n")
        from gas_optimizer import GasOptimizer
        opt = GasOptimizer(self.optimizer_dir)
        result = opt.optimize_contract(test_file)
        assert result["status"] == "success"
        assert any("Post-increment" in f["issue"] for f in result["findings"])

    def test_handles_missing_file(self):
        from gas_optimizer import GasOptimizer
        opt = GasOptimizer(self.optimizer_dir)
        result = opt.optimize_contract("/nonexistent/file.sol")
        assert result["status"] == "error"


class TestFuzzEngine:
    """Test the Foundry fuzz testing engine."""

    def test_skips_without_foundry_toml(self, tmp_path):
        from fuzz_engine import FuzzEngine
        engine = FuzzEngine(str(tmp_path))
        assert engine.has_foundry is False
        result = engine.run_fuzz_tests()
        assert result["status"] == "skipped"

    def test_detects_foundry_toml(self, tmp_path):
        (tmp_path / "foundry.toml").write_text("[profile.default]")
        from fuzz_engine import FuzzEngine
        engine = FuzzEngine(str(tmp_path))
        assert engine.has_foundry is True


class TestSolanaScanner:
    """Test the Solana/Rust vulnerability scanner."""

    def test_skips_non_solana_project(self, tmp_path):
        from solana_scanner import SolanaScanner
        scanner = SolanaScanner(str(tmp_path))
        assert scanner.is_solana is False
        result = scanner.scan()
        assert result["status"] == "skipped"

    def test_detects_anchor_project(self, tmp_path):
        (tmp_path / "Anchor.toml").write_text("[programs]")
        from solana_scanner import SolanaScanner
        scanner = SolanaScanner(str(tmp_path))
        assert scanner.is_solana is True

    def test_finds_missing_signer_check(self, tmp_path):
        (tmp_path / "Anchor.toml").write_text("[programs]")
        programs_dir = tmp_path / "programs"
        programs_dir.mkdir()
        rust_file = programs_dir / "lib.rs"
        rust_file.write_text("pub fn handler(ctx: Context, info: AccountInfo) -> Result<()> { Ok(()) }")
        from solana_scanner import SolanaScanner
        scanner = SolanaScanner(str(tmp_path))
        result = scanner.scan()
        assert result["status"] == "success"
        assert result["findings_count"] >= 1


class TestGitHubCommenter:
    """Test the GitHub PR commenting module."""

    def test_initializes_without_env(self):
        from github_commenter import GitHubCommenter
        commenter = GitHubCommenter()
        assert commenter.pr_number is None
        assert commenter.commit_sha is None

    def test_skips_comment_without_context(self):
        from github_commenter import GitHubCommenter
        commenter = GitHubCommenter()
        # Should not raise any exception
        commenter.post_inline_comment("test.sol", 1, "test body")
        commenter.post_general_comment("test summary")
