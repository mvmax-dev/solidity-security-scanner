import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-950 to-black text-white selection:bg-blue-500/30 flex flex-col">
      <header className="border-b border-gray-800/60 bg-gray-950/50 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center font-bold shadow-lg shadow-blue-500/20">S</div>
            <span className="font-semibold text-lg tracking-tight">Scanner PRO</span>
          </div>
          <div>
            <button className="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2 rounded-full font-medium transition-all shadow-[0_0_15px_rgba(37,99,235,0.4)]">
              Connect Wallet
            </button>
          </div>
        </div>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center px-4 pt-20 pb-32 relative overflow-hidden">
        {/* Glow effect */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-blue-600/10 rounded-full blur-[120px] pointer-events-none" />

        <div className="max-w-3xl mx-auto text-center space-y-8 relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm font-medium">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            v2.0.0 is Live
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-400">
            Automated Web3 Security. <br /> Decentralized.
          </h1>
          
          <p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto">
            Secure your Ethereum, Base, and Solana smart contracts automatically on every Pull Request. Unlock AI Validation and Gas Optimization.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <button className="w-full sm:w-auto px-8 py-4 rounded-xl bg-white text-black font-semibold hover:bg-gray-100 transition-colors">
              Get Started
            </button>
            <button className="w-full sm:w-auto px-8 py-4 rounded-xl bg-gray-900 border border-gray-800 hover:border-gray-700 text-white font-semibold transition-colors">
              View Documentation
            </button>
          </div>
        </div>

        <div className="mt-24 w-full max-w-5xl mx-auto rounded-2xl border border-gray-800 bg-gray-900/50 backdrop-blur-sm p-8 shadow-2xl relative">
          <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-purple-500 rounded-t-2xl" />
          <div className="grid md:grid-cols-3 gap-8 text-left">
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-blue-500/20 flex items-center justify-center border border-blue-500/30 text-blue-400">🤖</div>
              <h3 className="font-semibold text-lg">AI Validation</h3>
              <p className="text-gray-400 text-sm">Eliminates 99% of false positives using advanced deep learning heuristics.</p>
            </div>
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center border border-purple-500/30 text-purple-400">⛽</div>
              <h3 className="font-semibold text-lg">Gas Optimizer</h3>
              <p className="text-gray-400 text-sm">Automatically identifies storage packing and loop optimization opportunities.</p>
            </div>
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-emerald-500/20 flex items-center justify-center border border-emerald-500/30 text-emerald-400">🛡️</div>
              <h3 className="font-semibold text-lg">Fuzz & Solana</h3>
              <p className="text-gray-400 text-sm">Native support for Foundry fuzzing and Solana Anchor Rust analysis.</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
