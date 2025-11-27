// app/page.tsx

type Highlight = {
  title: string;
  text: string;
};

const highlights: Highlight[] = [
  {
    title: "Electronics & Embedded Systems",
    text: "Studying digital circuits, PWM, MOSFET drivers, and microelectronics while applying concepts through experiments and simulations.",
  },
  {
    title: "Full-Stack Foundations",
    text: "Building skills in Java, JavaScript, HTML/CSS, and modern web frameworks to design and implement end-to-end applications.",
  },
  {
    title: "Discipline Through Sport",
    text: "State-level basketball athlete with experience across track, badminton, tennis, and swimming, shaping resilience and consistency.",
  },
];

export default function HomePage() {
  return (
    <div className="space-y-12 sm:space-y-14 mt-2">
      {/* Hero */}
      <section className="space-y-4">
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-semibold tracking-tight">
          Engineering student focused on electronics, full-stack development,
          and system-level problem solving.
        </h1>

        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          I am <span className="font-medium">Chirag R Karanth</span>, an
          undergraduate engineering student based in Bangalore. My interests
          span digital electronics, mathematical modelling, and building web
          applications. I enjoy understanding how hardware, software, and
          mathematics work together to solve practical problems.
        </p>

        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          Outside academics and projects, I compete as a state-level basketball
          player and train across multiple sports. The discipline and focus from
          sport strongly influence how I approach engineering work.
        </p>

        {/* Professional link strip */}
        <div className="flex flex-wrap gap-3 pt-2 text-xs sm:text-sm">
          <LinkChip href="mailto:youremail@example.com" label="Email" />
          <LinkChip href="https://github.com/your-github" label="GitHub" />
          <LinkChip
            href="https://linkedin.com/in/your-linkedin"
            label="LinkedIn"
          />
          <LinkChip href="https://your-resume-link.com" label="Resume" />
        </div>
      </section>

      {/* Highlights */}
      <section className="grid gap-4 md:grid-cols-3">
        {highlights.map((h) => (
          <div
            key={h.title}
            className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5"
          >
            <p className="text-[11px] font-semibold uppercase tracking-[0.2em] text-slate-400">
              {h.title}
            </p>
            <p className="mt-2 text-xs sm:text-sm text-slate-300">{h.text}</p>
          </div>
        ))}
      </section>

      {/* Navigation cards */}
      <section className="grid gap-4 md:grid-cols-3">
        <HomeCard
          title="About"
          href="/about"
          description="Background, academic focus, and how I connect engineering and sport."
        />
        <HomeCard
          title="Projects"
          href="/projects"
          description="Selected work across web development, problem solving, and electronics."
        />
        <HomeCard
          title="Articles"
          href="/articles"
          description="Technical notes and explanations written to consolidate understanding."
        />
      </section>
    </div>
  );
}

function HomeCard({
  title,
  href,
  description,
}: {
  title: string;
  href: string;
  description: string;
}) {
  return (
    <a
      href={href}
      className="group rounded-2xl border border-white/10 bg-white/5/5 hover:bg-white/10 transition p-4 sm:p-5 flex flex-col justify-between"
    >
      <div>
        <h2 className="text-sm sm:text-base font-semibold flex items-center gap-2">
          {title}
          <span className="text-xs text-violet-300 opacity-0 group-hover:opacity-100 transition">
            →
          </span>
        </h2>
        <p className="mt-2 text-xs sm:text-sm text-slate-300">{description}</p>
      </div>
      <p className="mt-3 text-[11px] text-slate-500 group-hover:text-violet-300">
        Open {title.toLowerCase()}
      </p>
    </a>
  );
}

function LinkChip({ href, label }: { href: string; label: string }) {
  const isExternal = href.startsWith("http");
  return (
    <a
      href={href}
      target={isExternal ? "_blank" : undefined}
      rel={isExternal ? "noreferrer" : undefined}
      className="px-3 py-1 rounded-full border border-white/10 bg-white/5/5 hover:border-violet-400/70 hover:bg-white/10 transition"
    >
      {label}
    </a>
  );
}
