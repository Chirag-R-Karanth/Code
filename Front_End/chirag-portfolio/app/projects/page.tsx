// app/projects/page.tsx

type Project = {
  title: string;
  role: string;
  description: string;
  tags: string[];
  status: "Completed" | "In Progress" | "Planned";
  link?: string;
};

const projects: Project[] = [
  {
    title: "Personal Portfolio v1",
    role: "Frontend Development · Deployment",
    description:
      "Designed and deployed an initial personal portfolio to present my profile, skills, and work. Used this project to learn practical aspects of layout, responsiveness, and hosting.",
    tags: ["Next.js", "Tailwind CSS", "Frontend"],
    status: "Completed",
    link: "https://chirag-r-karanth.vercel.app/",
  },
  {
    title: "Data Structures & Algorithms Practice",
    role: "Core CS · Problem Solving",
    description:
      "Implementing data structures and algorithms in Java to strengthen fundamentals. Includes practice with arrays, linked lists, recursion, mathematical reasoning problems, and coding challenge-style tasks.",
    tags: ["Java", "DSA"],
    status: "In Progress",
  },
  {
    title: "PWM and MOSFET Driver Experiments",
    role: "Circuit Design · Hardware",
    description:
      "Exploring PWM generation, comparator use, digital ramps, and MOSFET drivers. Connecting theoretical knowledge from microelectronics and digital circuits to breadboard implementations.",
    tags: ["Electronics", "PWM", "Hardware"],
    status: "In Progress",
  },
  {
    title: "Mathematics & Engineering Notes",
    role: "Documentation · Conceptual Understanding",
    description:
      "Planned collection of structured notes on Laplace transforms, Newton–Raphson, Taylor series, and vector calculus, focused on clarity and application to engineering problems.",
    tags: ["Mathematics", "MA221TA"],
    status: "Planned",
  },
];

export default function ProjectsPage() {
  return (
    <div className="space-y-6">
      <section className="space-y-3">
        <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight">
          Projects
        </h1>
        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          A selection of ongoing and planned work across web development,
          problem solving, and electronics. Many of these projects are learning
          driven: the primary goal is to deepen understanding and build
          reliable, reproducible workflows.
        </p>
      </section>

      <section className="grid gap-4 sm:gap-5 md:grid-cols-2">
        {projects.map((p) => (
          <article
            key={p.title}
            className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5 flex flex-col justify-between hover:border-violet-500/60 transition"
          >
            <div className="space-y-2">
              <div className="flex items-center justify-between gap-2">
                <h2 className="text-sm sm:text-base font-semibold">
                  {p.title}
                </h2>
                <span className="text-[10px] px-2 py-1 rounded-full border border-white/15 text-slate-300">
                  {p.status}
                </span>
              </div>
              <p className="text-[11px] sm:text-xs text-slate-400">{p.role}</p>
              <p className="text-xs sm:text-sm text-slate-300 mt-1">
                {p.description}
              </p>
              <div className="flex flex-wrap gap-2 mt-3">
                {p.tags.map((t) => (
                  <span
                    key={t}
                    className="text-[10px] px-2 py-1 rounded-full bg-white/5 text-slate-300"
                  >
                    {t}
                  </span>
                ))}
              </div>
            </div>
            {p.link && (
              <a
                href={p.link}
                target="_blank"
                rel="noreferrer"
                className="mt-4 text-xs sm:text-sm text-violet-300 hover:text-violet-200"
              >
                Visit project →
              </a>
            )}
          </article>
        ))}
      </section>
    </div>
  );
}
