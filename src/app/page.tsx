/**
 * Landing page for Tall Poppies Pōneke: editorial hero, the meetup method, and CTA.
 *
 * @returns The homepage section
 */
export default function HomePage() {
  return (
    <main id="main">
      <section className="mx-auto grid min-h-[100dvh] max-w-6xl items-center gap-16 px-6 py-24 lg:grid-cols-[1.05fr_0.95fr] lg:gap-20">
        <div className="reveal">
          <p className="inline-flex items-center gap-2 rounded-full border border-barrel-brown/15 px-4 py-1.5 font-mono text-[11px] uppercase tracking-[0.22em] text-hop-green-deep">
            <span className="h-1.5 w-1.5 rounded-full bg-hound-amber" aria-hidden="true" />
            Pōneke · meetups monthly
          </p>
          <h1 className="mt-8 font-display text-5xl leading-[1.02] tracking-tight text-barrel-brown md:text-7xl">
            Pōneke&apos;s tallest club.{' '}
            <em className="text-hound-amber-deep">Standing room only.</em>
          </h1>
          <p className="mt-7 max-w-md text-lg leading-relaxed text-barrel-brown/70">
            No ducking, no craning, no &quot;how&apos;s the weather up there?&quot; Just honest,
            matey meetups for tall people — good venues, good chat, and a table where everyone can
            see.
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-6">
            <a
              className="group inline-flex items-center gap-3 rounded-full bg-hound-amber py-2 pl-6 pr-2 font-semibold text-barrel-brown transition-all duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] hover:bg-hound-amber-deep hover:text-cream-head active:scale-[0.98]"
              href="/contact"
            >
              Join the next meetup
              <span
                className="flex h-9 w-9 items-center justify-center rounded-full bg-barrel-brown/10 transition-transform duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] group-hover:translate-x-0.5 group-hover:bg-cream-head/15"
                aria-hidden="true"
              >
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.5"
                >
                  <path d="M7 17 17 7M9 7h8v8" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
            </a>
            <a
              className="font-mono text-sm text-barrel-brown/70 underline decoration-barrel-brown/30 underline-offset-4 transition-colors duration-300 hover:text-hound-amber-deep hover:decoration-hound-amber-deep"
              href="/help"
            >
              How a meetup works
            </a>
          </div>
          <p className="mt-14 font-mono text-xs uppercase tracking-[0.18em] text-barrel-brown/70">
            Good headroom · long legs · honest chat
          </p>
        </div>

        <div className="reveal hidden lg:block" style={{ animationDelay: '150ms' }}>
          <div
            className="p-2 ring-1 ring-barrel-brown/10"
            style={{ borderRadius: '2rem', background: 'rgba(44,24,16,0.04)' }}
          >
            <figure
              className="group relative overflow-hidden"
              style={{ borderRadius: 'calc(2rem - 0.5rem)' }}
            >
              <img
                src="https://picsum.photos/seed/arborist/900/1100"
                alt="A Wellington bar with high ceilings and tall stools"
                className="aspect-[4/5] w-full object-cover transition-transform duration-700 ease-[cubic-bezier(0.32,0.72,0,1)] group-hover:scale-[1.04]"
                loading="lazy"
              />
              <figcaption className="absolute bottom-4 left-4 rounded-full bg-barrel-brown/85 px-4 py-2 font-mono text-xs text-cream-head backdrop-blur-md">
                High ceilings — Courtenay Place
              </figcaption>
            </figure>
          </div>
          <div
            className="mt-6 w-4/5 p-2 ring-1 ring-barrel-brown/10 lg:ml-16 lg:rotate-[1.5deg]"
            style={{ borderRadius: '2rem', background: 'rgba(44,24,16,0.04)' }}
          >
            <figure
              className="group relative overflow-hidden"
              style={{ borderRadius: 'calc(2rem - 0.5rem)' }}
            >
              <img
                src="https://picsum.photos/seed/goldings/900/1100"
                alt="A group of tall friends laughing at a Cuba Street table"
                className="aspect-[4/5] w-full object-cover transition-transform duration-700 ease-[cubic-bezier(0.32,0.72,0,1)] group-hover:scale-[1.04]"
                loading="lazy"
              />
              <figcaption className="absolute bottom-4 left-4 rounded-full bg-barrel-brown/85 px-4 py-2 font-mono text-xs text-cream-head backdrop-blur-md">
                Back table booked — Cuba St
              </figcaption>
            </figure>
          </div>
        </div>
      </section>

      <section className="border-t border-barrel-brown/10 bg-pint-pour/60">
        <div className="mx-auto grid max-w-6xl gap-16 px-6 py-28 lg:grid-cols-[0.85fr_1.15fr] lg:gap-24">
          <div className="reveal lg:sticky lg:top-24 lg:self-start">
            <p className="font-mono text-[11px] uppercase tracking-[0.22em] text-hop-green-deep">
              The meetup method
            </p>
            <h2 className="mt-5 font-display text-4xl leading-tight tracking-tight md:text-5xl">
              Three steps to a good night.
            </h2>
            <p className="mt-5 max-w-sm leading-relaxed text-barrel-brown/70">
              Every meetup gets the same treatment: scout the venue, gather the crew, then toast the
              night. No venue gets picked twice unless it earns it.
            </p>
            <a
              className="mt-8 inline-block font-mono text-sm text-hound-amber-deep underline decoration-hound-amber-deep/30 underline-offset-4 transition-colors duration-300 hover:decoration-hound-amber-deep"
              href="/help"
            >
              Read the full method
            </a>
          </div>

          <div>
            {[
              {
                n: '01',
                title: 'Scout',
                body: 'We find venues with headroom, good light, and a table that fits a tall crew.',
                accent: 'text-hop-green-deep',
              },
              {
                n: '02',
                title: 'Gather',
                body: 'We pick a date, post it, and book the back table. RSVP and show up — that&apos;s it.',
                accent: 'text-southerly-blue',
              },
              {
                n: '03',
                title: 'Toast',
                body: 'Glasses raised, no ducking. One honest verdict: worth your Saturday, or not.',
                accent: 'text-hound-amber-deep',
              },
            ].map((step, i) => (
              <article
                key={step.n}
                className="reveal border-t border-barrel-brown/10 py-10 first:border-t-0"
                style={{ animationDelay: `${i * 120}ms` }}
              >
                <div className="flex items-baseline gap-6">
                  <span className={`font-mono text-sm font-medium ${step.accent}`}>{step.n}</span>
                  <h3 className="font-display text-2xl tracking-tight">{step.title}</h3>
                </div>
                <p className="mt-3 max-w-md pl-14 leading-relaxed text-barrel-brown/70">
                  {step.body}
                </p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 pb-28 pt-4">
        <div className="reveal relative mx-auto max-w-6xl overflow-hidden rounded-[2.5rem] bg-barrel-brown px-8 py-24 text-center text-cream-head md:py-32">
          <div
            className="pointer-events-none absolute -right-32 -top-32 h-96 w-96 rounded-full bg-hound-amber/20 blur-3xl"
            aria-hidden="true"
          />
          <div
            className="pointer-events-none absolute -bottom-40 -left-24 h-80 w-80 rounded-full bg-southerly-blue/20 blur-3xl"
            aria-hidden="true"
          />
          <div className="relative mx-auto max-w-2xl">
            <p className="font-mono text-[11px] uppercase tracking-[0.22em] text-hound-amber">
              Crowd-led · local-first
            </p>
            <h2 className="mt-6 font-display text-4xl leading-tight tracking-tight md:text-6xl">
              Know a tall-friendly spot?
            </h2>
            <p className="mx-auto mt-6 max-w-md leading-relaxed text-cream-head/70">
              If a venue has ceilings you can stand under, we want to hear about it.
            </p>
            <a
              className="group mt-10 inline-flex items-center gap-3 rounded-full bg-hound-amber py-2 pl-6 pr-2 font-semibold text-barrel-brown transition-all duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] hover:bg-cream-head active:scale-[0.98]"
              href="/feedback"
            >
              Send us a tip
              <span
                className="flex h-9 w-9 items-center justify-center rounded-full bg-barrel-brown/10 transition-transform duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] group-hover:translate-x-0.5"
                aria-hidden="true"
              >
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.5"
                >
                  <path d="M7 17 17 7M9 7h8v8" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
            </a>
          </div>
        </div>
      </section>

      <footer className="border-t border-barrel-brown/10">
        <div className="mx-auto flex max-w-6xl flex-col gap-6 px-6 py-12 md:flex-row md:items-center md:justify-between">
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-barrel-brown/70">
            Tall Poppies · Pōneke
          </p>
          <nav
            aria-label="Footer"
            className="flex flex-wrap gap-6 font-mono text-sm text-barrel-brown/70"
          >
            <a className="transition-colors duration-300 hover:text-hound-amber-deep" href="/help">
              Help
            </a>
            <a
              className="transition-colors duration-300 hover:text-hound-amber-deep"
              href="/contact"
            >
              Contact
            </a>
            <a
              className="transition-colors duration-300 hover:text-hound-amber-deep"
              href="/feedback"
            >
              Feedback
            </a>
          </nav>
        </div>
      </footer>
    </main>
  );
}
