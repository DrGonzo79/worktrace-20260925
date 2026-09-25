import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"WorkTrace — robotics task capture planner",description:"Build a fictional field-data capture plan for skilled-trade robotics training."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
