import TerminalDemo from '@/components/TerminalDemo';

export default function Home() {
  return (
    <div className="min-h-screen relative selection:bg-purple-500/30">
      {/* Background Orbs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none -z-10">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-purple-900/20 blur-[120px] mix-blend-screen"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] rounded-full bg-teal-900/20 blur-[120px] mix-blend-screen"></div>
      </div>

      {/* Navigation */}
      <nav className="fixed w-full z-50 glass-panel border-b-0 border-x-0 rounded-none bg-black/40">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded bg-gradient-to-br from-purple-500 to-teal-400 flex items-center justify-center font-bold text-white shadow-[0_0_15px_rgba(157,78,221,0.5)]">
              S
            </div>
            <span className="font-bold text-xl tracking-tight text-white">Scanner<span className="text-purple-400">PRO</span></span>
          </div>
          <div className="hidden md:flex items-center gap-8 text-sm font-medium text-gray-300">
            <a href="#features" className="hover:text-white transition-colors">Features</a>
            <a href="#how-it-works" className="hover:text-white transition-colors">How it Works</a>
            <a href="#pricing" className="hover:text-white transition-colors">Pricing</a>
          </div>
          <button className="bg-white text-black px-6 py-2.5 rounded-full text-sm font-semibold hover:bg-gray-100 transition-all hover:scale-105 shadow-[0_0_20px_rgba(255,255,255,0.2)]">
            Install to GitHub
          </button>
        </div>
      </nav>

      <main>
        {/* Hero Section */}
        <section className="pt-40 pb-20 px-6 min-h-[90vh] flex flex-col items-center justify-center relative">
          <div className="max-w-4xl mx-auto text-center z-10">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full glass-panel mb-8 border-purple-500/30">
              <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span>
              <span className="text-xs font-medium text-purple-200">v2.2 Enterprise Release is Live</span>
            </div>
            
            <h1 className="text-6xl md:text-8xl font-black tracking-tighter text-white mb-6 leading-tight">
              Secure Web3 <br/>
              <span className="gradient-text">Faster.</span>
            </h1>
            
            <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed">
              The #1 AI-powered smart contract auditor for GitHub CI/CD. 
              Find reentrancy, optimize gas, and suppress false positives instantly.
            </p>
            
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-20">
              <button className="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-purple-600 to-indigo-600 text-white rounded-lg font-bold text-lg hover:from-purple-500 hover:to-indigo-500 transition-all shadow-[0_0_30px_rgba(157,78,221,0.4)] animate-glow">
                Start Free Trial
              </button>
              <button className="w-full sm:w-auto px-8 py-4 glass-panel text-white rounded-lg font-bold text-lg hover:bg-white/10 transition-all">
                View Documentation
              </button>
            </div>
          </div>

          {/* Terminal Demo Component */}
          <div className="w-full relative z-10 px-4 md:px-0">
            <TerminalDemo />
          </div>
        </section>

        {/* Logos Section */}
        <section className="py-10 border-y border-white/5 bg-black/20 backdrop-blur-sm">
          <div className="max-w-7xl mx-auto px-6">
            <p className="text-center text-sm font-medium text-gray-500 mb-6 uppercase tracking-widest">Securing smart contracts across</p>
            <div className="flex flex-wrap justify-center items-center gap-12 opacity-50 grayscale hover:grayscale-0 transition-all duration-500">
              {/* Replace with actual SVGs in production */}
              <div className="text-2xl font-bold font-mono">ETHEREUM</div>
              <div className="text-2xl font-bold font-mono text-blue-500">BASE</div>
              <div className="text-2xl font-bold font-mono text-purple-500">SOLANA</div>
              <div className="text-2xl font-bold font-mono text-red-500">OPTIMISM</div>
            </div>
          </div>
        </section>

        {/* Features Grid */}
        <section id="features" className="py-32 px-6 relative">
          <div className="max-w-7xl mx-auto">
            <div className="text-center mb-20">
              <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">Enterprise-Grade Security</h2>
              <p className="text-gray-400">Everything you need to deploy to mainnet with absolute confidence.</p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {[
                { title: "Deep AST Analysis", desc: "Analyzes Solidity & Rust Abstract Syntax Trees to find logic flaws that static Regex misses.", icon: "🌳" },
                { title: "AI False-Positive Suppression", desc: "Tired of noisy Slither alerts? Our AI validator suppresses 99% of false positives automatically.", icon: "🤖" },
                { title: "AST Gas Optimizer", desc: "Identifies uncached variables and improper packing, calculating exact gas savings per line.", icon: "⛽" },
                { title: "Inline PR Comments", desc: "No context switching. Get vulnerability reports directly on your GitHub Pull Request lines.", icon: "💬" },
                { title: "Multi-Chain Engine", desc: "Native support for EVM (Solidity/Vyper) and Solana (Rust/Anchor) in a single workflow.", icon: "⛓️" },
                { title: "Foundry Fuzzing", desc: "Automatically triggers and analyzes Foundry fuzz tests to catch edge-case exploits.", icon: "🎯" }
              ].map((f, i) => (
                <div key={i} className="glass-panel p-8 rounded-2xl hover:-translate-y-2 transition-transform duration-300">
                  <div className="text-4xl mb-4">{f.icon}</div>
                  <h3 className="text-xl font-bold text-white mb-3">{f.title}</h3>
                  <p className="text-gray-400 text-sm leading-relaxed">{f.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Pricing Section */}
        <section id="pricing" className="py-32 px-6 bg-black/40 border-t border-white/5 relative">
          <div className="max-w-7xl mx-auto">
            <div className="text-center mb-20">
              <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">Transparent Pricing</h2>
              <p className="text-gray-400">Pay in Crypto (Web3 Native) or Fiat (Enterprise).</p>
            </div>

            <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
              {/* Free Tier */}
              <div className="glass-panel p-8 rounded-3xl border border-white/10">
                <h3 className="text-2xl font-bold text-white mb-2">Open Source</h3>
                <div className="text-4xl font-black text-white mb-6">$0<span className="text-lg text-gray-500 font-normal">/forever</span></div>
                <p className="text-gray-400 text-sm mb-8">Basic structural analysis for public repositories.</p>
                <ul className="space-y-4 mb-8 text-sm text-gray-300">
                  <li className="flex items-center gap-2">✓ AST Structural Scanning</li>
                  <li className="flex items-center gap-2">✓ Inline PR Comments</li>
                  <li className="flex items-center gap-2 text-gray-600">✗ AI False-Positive Filter</li>
                  <li className="flex items-center gap-2 text-gray-600">✗ Gas Optimization Engine</li>
                </ul>
                <button className="w-full py-3 rounded-lg glass-panel text-white font-medium hover:bg-white/10 transition-colors">
                  Install Free Action
                </button>
              </div>

              {/* Pro Tier (Metered) */}
              <div className="glass-panel p-8 rounded-3xl border border-purple-500/50 relative transform md:-translate-y-4 shadow-[0_0_30px_rgba(157,78,221,0.2)]">
                <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white text-xs font-bold px-4 py-1 rounded-full uppercase tracking-wider">
                  Most Popular
                </div>
                <h3 className="text-2xl font-bold text-white mb-2">Web3 Indie</h3>
                <div className="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-teal-400 mb-6">
                  Metered
                </div>
                <p className="text-gray-400 text-sm mb-8">Deposit USDC. Pay per scan using x402 Web3 Treasury logic.</p>
                <ul className="space-y-4 mb-8 text-sm text-white">
                  <li className="flex items-center gap-2">✓ Everything in Free</li>
                  <li className="flex items-center gap-2">✓ AI False-Positive Suppression</li>
                  <li className="flex items-center gap-2">✓ AST Gas Optimizer Engine</li>
                  <li className="flex items-center gap-2">✓ Pay via USDC (Base/Eth)</li>
                </ul>
                <button className="w-full py-3 rounded-lg bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold hover:from-purple-500 hover:to-indigo-500 transition-colors">
                  Deposit 20 USDC
                </button>
              </div>

              {/* Enterprise Tier */}
              <div className="glass-panel p-8 rounded-3xl border border-white/10">
                <h3 className="text-2xl font-bold text-white mb-2">Enterprise</h3>
                <div className="text-4xl font-black text-white mb-6">Custom</div>
                <p className="text-gray-400 text-sm mb-8">For large teams needing fiat invoicing and SLAs.</p>
                <ul className="space-y-4 mb-8 text-sm text-gray-300">
                  <li className="flex items-center gap-2">✓ Everything in PRO</li>
                  <li className="flex items-center gap-2">✓ Pay via Stripe (Fiat)</li>
                  <li className="flex items-center gap-2">✓ Dedicated Support SLA</li>
                  <li className="flex items-center gap-2">✓ Custom Rule Generation</li>
                </ul>
                <button className="w-full py-3 rounded-lg bg-white text-black font-medium hover:bg-gray-200 transition-colors">
                  Contact Sales
                </button>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="py-12 border-t border-white/10 text-center text-gray-500 text-sm">
        <p>© 2026 Maxwell VOSS Security. All rights reserved.</p>
        <p className="mt-2">Built for the Web3 Security Community.</p>
      </footer>
    </div>
  );
}
