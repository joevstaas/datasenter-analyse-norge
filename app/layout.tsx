import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata={title:'Datasentre i Norge | Ocean Data Jo Labs',description:'Utforsk kraft, areal, natur og eierskap i et kildebelagt prosjektutvalg. KI-drevet demo, ikke beslutningsstøtte.',robots:{index:false,follow:false}};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="nb"><body>{children}</body></html>;}
