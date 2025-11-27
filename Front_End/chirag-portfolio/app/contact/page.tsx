// app/contact/page.tsx

export default function ContactPage() {
  return (
    <div className="space-y-8 max-w-3xl">
      <section className="space-y-3">
        <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight">
          Contact
        </h1>
        <p className="text-sm sm:text-base text-slate-300 leading-relaxed">
          I am open to opportunities related to internships, collaborative
          projects, and technical discussions around electronics, software
          development, or sports and performance. The best way to reach me is
          via email or through the profiles below.
        </p>
      </section>

      <section className="space-y-4">
        <div className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5">
          <h2 className="text-sm sm:text-base font-semibold">Email</h2>
          <p className="mt-1 text-xs sm:text-sm text-slate-300">
            <a
              href="mailto:youremail@example.com"
              className="text-violet-300 hover:text-violet-200"
            >
              youremail@example.com
            </a>
          </p>
        </div>

        <div className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5 space-y-2">
          <h2 className="text-sm sm:text-base font-semibold">Profiles</h2>
          <ul className="text-xs sm:text-sm text-slate-300 space-y-1">
            <li>
              GitHub:{" "}
              <a
                href="https://github.com/your-github"
                target="_blank"
                rel="noreferrer"
                className="text-violet-300 hover:text-violet-200"
              >
                @your-github
              </a>
            </li>
            <li>
              LinkedIn:{" "}
              <a
                href="https://linkedin.com/in/your-linkedin"
                target="_blank"
                rel="noreferrer"
                className="text-violet-300 hover:text-violet-200"
              >
                your-linkedin
              </a>
            </li>
          </ul>
          <p className="mt-2 text-[11px] text-slate-500">
            Replace these placeholders with your actual contact details and
            profile links.
          </p>
        </div>
      </section>
    </div>
  );
}
