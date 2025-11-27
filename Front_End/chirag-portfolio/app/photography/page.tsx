// app/photography/page.tsx

type Shot = {
  title: string;
  context: string;
  description: string;
};

const shots: Shot[] = [
  {
    title: "Courtside",
    context: "Basketball and training environments",
    description:
      "Moments from practices and games, focusing on movement, intensity, and teamwork. Sports photography helps capture the environment I spend much of my time in.",
  },
  {
    title: "Urban Evenings",
    context: "Bangalore city",
    description:
      "Scenes from the city during late hours: traffic, light, and atmosphere. A contrast to structured academic and training schedules.",
  },
  {
    title: "Details & Still Frames",
    context: "Everyday surroundings",
    description:
      "Small details from ordinary locations that are easy to miss in a busy routine. Photography and editing offer a different way to slow down and observe.",
  },
];

export default function PhotographyPage() {
  return (
    <div className="space-y-6 sm:space-y-8">
      <section className="space-y-3">
        <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight">
          Photography
        </h1>
        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          I use photography and basic video editing as a way to document the
          environments I am part of—courts, cities, and everyday spaces. Over
          time, I plan to showcase selected work here as a visual complement to
          my technical projects.
        </p>
        <p className="text-[11px] sm:text-xs text-slate-500">
          This page currently describes themes. It can be extended with real
          photo grids or gallery links in future iterations.
        </p>
      </section>

      <section className="grid gap-4 sm:gap-5 md:grid-cols-3">
        {shots.map((shot) => (
          <article
            key={shot.title}
            className="rounded-2xl border border-white/10 bg-white/5/5 p-4 sm:p-5 flex flex-col justify-between"
          >
            <div>
              <h2 className="text-sm sm:text-base font-semibold">
                {shot.title}
              </h2>
              <p className="text-[11px] sm:text-xs text-slate-400 mt-1">
                {shot.context}
              </p>
            </div>
            <p className="mt-2 text-xs sm:text-sm text-slate-300">
              {shot.description}
            </p>
          </article>
        ))}
      </section>
    </div>
  );
}
