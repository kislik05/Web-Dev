import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  { 
    path: '', 
    loadChildren: () => import('./app.routes').then(m => m.routes),
    renderMode: RenderMode.Server
  }
];