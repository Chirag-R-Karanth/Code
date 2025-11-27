// app/layout.tsx
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Chirag R Karanth",
  description:
    "Engineering student specializing in electronics, full-stack development, and systems thinking.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-[#050712] text-slate-100 min-h-screen antialiased">
        {/* Accent bar */}
        <div className="h-1 w-full bg-gradient-to-r from-violet-500 via-indigo-500 to-emerald-400" />

        <div className="max-w-5xl mx-auto px-4 sm:px-6">
          {/* Header */}
          <header className="py-6 sm:py-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div className="space-y-1">
              <p className="text-xs font-semibold tracking-[0.3em] uppercase text-slate-400">
                Chirag R Karanth
              </p>
              <p className="text-xs text-slate-500">
                Electronics · Full-Stack Development · Sports
              </p>
            </div>

            <nav className="flex flex-wrap items-center gap-2 text-xs sm:text-sm">
              <NavLink href="/">Home</NavLink>
              <NavLink href="/about">About</NavLink>
              <NavLink href="/projects">Projects</NavLink>
              <NavLink href="/articles">Articles</NavLink>
              <NavLink href="/photography">Photography</NavLink>
              <NavLink href="/contact">Contact</NavLink>
            </nav>
          </header>

          <main className="pb-12 sm:pb-16">{children}</main>

          <footer className="border-t border-white/5 py-4 text-[11px] sm:text-xs text-slate-500 flex flex-col sm:flex-row gap-1 sm:items-center sm:justify-between">
            <p>© {new Date().getFullYear()} Chirag R Karanth</p>
            <p>Built with Next.js and Tailwind CSS.</p>
          </footer>
        </div>
      </body>
    </html>
  );
}

function NavLink({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) {
  return (
    <a
      href={href}
      className="px-3 py-1 rounded-full border border-transparent hover:border-violet-500/70 hover:bg-white/5 transition"
    >
      {children}
    </a>
  );
}
