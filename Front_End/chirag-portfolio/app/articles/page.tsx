// app/articles/page.tsx

type Article = {
  title: string;
  date: string;
  summary: string;
  tags: string[];
};

const articles: Article[] = [
  {
    title: "Understanding PWM: From Digital Ramp to MOSFET Driver",
    date: "November 2025",
    summary:
      "An explanation of how digital ramps, comparators, and MOSFETs interact in a PWM circuit, and how this connects to driver design.",
    tags: ["Electronics", "PWM"],
  },
  {
    title: "Laplace Transforms in Engineering Practice",
    date: "October 2025",
    summary:
      "A structured view of Laplace transforms, inverse transforms, and their application to solving linear differential equations.",
    tags: ["Mathematics", "MA221TA"],
  },
  {
    title: "Configuring javac, gcc, and git on Windows with WSL",
    date: "September 2025",
    summary:
      "Notes from resolving PATH and environment issues when using compilers and development tools across Windows and WSL.",
    tags: ["Dev Environment", "Windows", "WSL"],
  },
  {
    title: "Training, Core Strength, and Multi-Sport Performance",
    date: "July 2025",
    summary:
      "Reflections on managing cramps, back pain, and core strength while balancing basketball, track, badminton, and tennis.",
    tags: ["Sports", "Training"],
  },
];

export default function ArticlesPage() {
  return (
    <div className="space-y-6">
      <section className="space-y-3">
        <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight">
          Articles & Technical Notes
        </h1>
        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          These notes are written primarily for my own understanding, with the
          goal of turning complex topics into clear, reusable explanations. They
          cover electronics, mathematics, development environments, and
          training-related observations.
        </p>
      </section>

      <section className="space-y-3">
        {articles.map((a) => (
          <article
            key={a.title}
            className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5 hover:border-emerald-400/60 transition"
          >
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
              <h2 className="text-sm sm:text-base font-semibold">{a.title}</h2>
              <p className="text-[11px] sm:text-xs text-slate-400">{a.date}</p>
            </div>
            <p className="mt-2 text-xs sm:text-sm text-slate-300">
              {a.summary}
            </p>
            <div className="flex flex-wrap gap-2 mt-3">
              {a.tags.map((t) => (
                <span
                  key={t}
                  className="text-[10px] px-2 py-1 rounded-full bg-white/5 text-slate-300"
                >
                  {t}
                </span>
              ))}
            </div>
          </article>
        ))}
      </section>
    </div>
  );
}
