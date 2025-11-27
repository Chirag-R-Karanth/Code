// app/about/page.tsx

export default function AboutPage() {
  return (
    <div className="space-y-10">
      <section className="space-y-4">
        <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight">
          About
        </h1>
        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          I am an undergraduate engineering student at{" "}
          <span className="font-medium">RV College of Engineering</span> in
          Bangalore. My academic and technical interests include digital
          electronics, embedded systems, applied mathematics, and full-stack web
          development. I enjoy working through complex topics systematically and
          connecting theoretical concepts to implementation.
        </p>
      </section>

      <section className="grid gap-8 md:grid-cols-2">
        <div className="space-y-3">
          <h2 className="text-sm font-semibold tracking-[0.2em] uppercase text-slate-400">
            Engineering & Technology
          </h2>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            At RVCE, I study subjects such as analog microelectronics, analysis
            and design of digital circuits, network and control systems, and
            advanced engineering mathematics. Alongside this, I am building
            skills in Java, Python, C, and JavaScript, with a growing focus on
            full-stack development using modern web frameworks.
          </p>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            I am particularly interested in how hardware and software interact.
            This includes experimenting with PWM generation, MOSFET driver
            circuits, 555 timers, and using tools like Logisim and Arduino to
            validate digital and analog concepts.
          </p>
        </div>

        <div className="space-y-3">
          <h2 className="text-sm font-semibold tracking-[0.2em] uppercase text-slate-400">
            Sports & Discipline
          </h2>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            I compete as a state-level basketball player and actively train in
            track, badminton, tennis, and swimming, where I have also earned
            medals. Competitive sport has taught me consistency, resilience,
            time management, and how to handle high-pressure situations.
          </p>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            These qualities strongly influence my approach to engineering:
            breaking down complex problems, working through setbacks, and
            maintaining focus over long periods of study and project work.
          </p>
        </div>
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold tracking-[0.2em] uppercase text-slate-400">
          Areas of Interest
        </h2>
        <ul className="list-disc list-inside text-xs sm:text-sm text-slate-300 space-y-2">
          <li>Digital electronics, logic design, and microelectronics.</li>
          <li>PWM, signal generation, and basic power electronics.</li>
          <li>
            Full-stack web development using JavaScript, React, and Next.js.
          </li>
          <li>Data structures, algorithms, and problem solving in Java.</li>
          <li>Applied mathematics: Laplace transforms, numerical methods.</li>
        </ul>
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold tracking-[0.2em] uppercase text-slate-400">
          Technical Skills
        </h2>
        <div className="grid gap-4 md:grid-cols-2 text-xs sm:text-sm text-slate-300">
          <div>
            <p className="font-medium text-slate-200">Programming</p>
            <p>Java, Python, C, C++, JavaScript</p>
          </div>
          <div>
            <p className="font-medium text-slate-200">Web</p>
            <p>HTML, CSS, React, Next.js, basic REST concepts</p>
          </div>
          <div>
            <p className="font-medium text-slate-200">Electronics</p>
            <p>Logisim, Arduino, PWM experiments, 555 timer circuits</p>
          </div>
          <div>
            <p className="font-medium text-slate-200">Tools & Systems</p>
            <p>Git, Linux/WSL, VS Code, Windows 10</p>
          </div>
        </div>
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold tracking-[0.2em] uppercase text-slate-400">
          Education
        </h2>
        <div className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5">
          <h3 className="text-sm sm:text-base font-semibold">
            RV College of Engineering
          </h3>
          <p className="text-xs text-slate-400 mt-1">Bangalore, India</p>
          <p className="text-xs sm:text-sm text-slate-300 mt-2">
            Bachelor of Engineering with coursework in analog microelectronics,
            analysis and design of digital circuits, network and control
            systems, engineering mathematics, and chemistry of functional
            materials.
          </p>
        </div>
      </section>
    </div>
  );
}
