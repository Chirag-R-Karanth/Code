// app/uses/page.tsx

export default function UsesPage() {
  return (
    <div className="space-y-8">
      <section className="space-y-3">
        <h1 className="text-2xl md:text-3xl font-semibold tracking-tight">
          Current config.
        </h1>
        <p className="text-sm md:text-base text-neutral-300 leading-relaxed">
          The tools and gear I use to write code, design circuits, study, play,
          and try to keep life somewhat organised.
        </p>
      </section>

      <section className="space-y-4">
        <h2 className="text-xs md:text-sm font-medium tracking-[0.2em] uppercase text-neutral-500">
          Hardware
        </h2>
        <ul className="space-y-2 text-sm md:text-base text-neutral-300">
          <li>
            <span className="font-medium">Main laptop</span> – Windows 10
            machine that does everything from coding to watching anime and
            gaming. Nothing crazy, but enough to run IDEs, WSL, and a browser
            full of tabs.
          </li>
          <li>
            <span className="font-medium">External SSD</span> – Used for extra
            storage and fast project access. I&apos;ve fought with it showing up
            as offline / &quot;internal&quot; more times than I&apos;d like to
            admit.
          </li>
          <li>
            <span className="font-medium">Phone + headphones</span> – For
            lectures, music while coding, and watching F1 highlights.
          </li>
        </ul>
      </section>

      <section className="space-y-4">
        <h2 className="text-xs md:text-sm font-medium tracking-[0.2em] uppercase text-neutral-500">
          Development
        </h2>
        <ul className="space-y-2 text-sm md:text-base text-neutral-300">
          <li>
            <span className="font-medium">VS Code</span> – My main editor for
            Java, Python, JavaScript, and everything else. Extensions for
            formatting, IntelliSense, and Git integration keep me sane.
          </li>
          <li>
            <span className="font-medium">WSL + Linux distros</span> – I like
            having a real Linux environment inside Windows. I&apos;ve played
            with distros like Arch and spent plenty of time solving PATH and
            config issues.
          </li>
          <li>
            <span className="font-medium">Java toolchain</span> – JDK +
            terminal + simple build configs while I work through OOP,
            inheritance, exceptions, interfaces, and multithreading.
          </li>
          <li>
            <span className="font-medium">Logisim</span> – For digital circuit
            design. Great for visualising what&apos;s actually happening inside
            adders, counters, and simple CPUs.
          </li>
          <li>
            <span className="font-medium">Arduino / basic electronics tools</span>{" "}
            – For messing around with PWM, drivers, and hardware experiments.
          </li>
        </ul>
      </section>

      <section className="space-y-4">
        <h2 className="text-xs md:text-sm font-medium tracking-[0.2em] uppercase text-neutral-500">
          Media & Design
        </h2>
        <ul className="space-y-2 text-sm md:text-base text-neutral-300">
          <li>
            <span className="font-medium">Photo & video editing tools</span> – I
            enjoy photography and videography, and I use common editing software
            to cut, grade, and share moments from sports or life.
          </li>
          <li>
            <span className="font-medium">Simple design tools</span> – Whatever
            is quickest to mock up an idea or visual without getting stuck in
            perfectionism.
          </li>
        </ul>
      </section>

      <section className="space-y-4">
        <h2 className="text-xs md:text-sm font-medium tracking-[0.2em] uppercase text-neutral-500">
          Productivity
        </h2>
        <ul className="space-y-2 text-sm md:text-base text-neutral-300">
          <li>
            A mix of calendars, reminders, and notes to juggle college
            schedules, sports, and coding. I&apos;m still figuring out a system
            that&apos;s strict enough to keep me on track but flexible enough to
            survive real life.
          </li>
          <li>
            I care a lot about efficiency and control over my tools, so I prefer
            setups that I can tweak rather than black-box solutions.
          </li>
        </ul>
      </section>
    </div>
  );
}
