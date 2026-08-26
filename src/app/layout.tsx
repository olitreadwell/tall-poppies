import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { DM_Mono, Geist, Playfair_Display } from 'next/font/google';
import './globals.css';

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-playfair',
});

const geist = Geist({
  subsets: ['latin'],
  variable: '--font-geist',
});

const dmMono = DM_Mono({
  weight: ['400', '500'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  variable: '--font-dm-mono',
});

export const metadata: Metadata = {
  title: 'Tall Poppies Pōneke',
  description: "Pōneke's meetup for tall people — good venues, good chat, no ducking.",
};

/**
 * Root layout: wraps every route in the HTML shell.
 *
 * @param props - Layout props
 * @param props.children - Rendered route content
 * @returns The root HTML document
 */
export default function RootLayout({ children }: Readonly<{ children: ReactNode }>): ReactNode {
  return (
    <html lang="en">
      <body className={`${playfair.variable} ${geist.variable} ${dmMono.variable}`}>
        <header>
          <a
            className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] focus:rounded-md focus:bg-hound-amber focus:px-4 focus:py-2 focus:font-semibold focus:text-barrel-brown"
            href="#main"
          >
            Skip to content
          </a>
        </header>
        {children}
      </body>
    </html>
  );
}
