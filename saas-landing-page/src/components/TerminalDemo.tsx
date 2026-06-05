"use client";

import { useState, useEffect } from 'react';

const TerminalDemo = () => {
  const [lines, setLines] = useState<string[]>([]);
  
  const demoSequence = [
    { text: "$ openclaw scan ./contracts", delay: 800, type: "input" },
    { text: "Initializing Deep AST Analysis...", delay: 1200, type: "info" },
    { text: "Scanning 14 contracts across 3 chains...", delay: 2000, type: "info" },
    { text: "⚠️ [CRITICAL] Reentrancy detected in Vault.sol:47", delay: 2800, type: "error" },
    { text: "   Location: external call `msg.sender.call{value: amount}()` before state update.", delay: 3000, type: "detail" },
    { text: "   AI Validator: True Positive. Exploit path verified via Slither integration.", delay: 3500, type: "detail" },
    { text: "⛽ [GAS] Optimization found in Loop.sol:21", delay: 4200, type: "success" },
    { text: "   Suggestion: Cache array length `uint256 len = arr.length;`", delay: 4500, type: "detail" },
    { text: "   Estimated Savings: 2,400 Gas per transaction.", delay: 4800, type: "detail" },
    { text: "Scan complete. 1 Critical, 0 High, 1 Optimization.", delay: 5500, type: "info" },
    { text: "Report generated and PR comment posted. ✅", delay: 6000, type: "success" }
  ];

  useEffect(() => {
    let timeouts: NodeJS.Timeout[] = [];
    
    demoSequence.forEach((item, index) => {
      const timeout = setTimeout(() => {
        setLines(prev => [...prev, item]);
      }, item.delay);
      timeouts.push(timeout);
    });

    return () => timeouts.forEach(t => clearTimeout(t));
  }, []);

  return (
    <div className="terminal-window p-6 text-sm w-full max-w-2xl mx-auto shadow-2xl relative overflow-hidden glass-panel rounded-xl">
      <div className="flex gap-2 mb-4">
        <div className="w-3 h-3 rounded-full bg-red-500"></div>
        <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
        <div className="w-3 h-3 rounded-full bg-green-500"></div>
      </div>
      <div className="space-y-2 min-h-[300px]">
        {lines.map((line, i) => (
          <div key={i} className={`
            ${(line as any).type === 'input' ? 'text-white font-bold' : ''}
            ${(line as any).type === 'info' ? 'text-blue-400' : ''}
            ${(line as any).type === 'error' ? 'text-red-500 font-semibold' : ''}
            ${(line as any).type === 'success' ? 'text-green-400' : ''}
            ${(line as any).type === 'detail' ? 'text-gray-400 pl-4' : ''}
          `}>
            {line.text}
          </div>
        ))}
        {lines.length < demoSequence.length && (
          <div className="animate-pulse w-2 h-4 bg-gray-400 mt-2"></div>
        )}
      </div>
      
      {/* Decorative Blur */}
      <div className="absolute -top-20 -right-20 w-40 h-40 bg-purple-600 rounded-full mix-blend-multiply filter blur-[64px] opacity-30 animate-pulse"></div>
    </div>
  );
};

export default TerminalDemo;
