import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.isLoggedIn()) {
    // Se è richiesta una verifica del ruolo
    const requiredRole = route.data['role'];
    if (requiredRole && !authService.hasRole(requiredRole)) {
      router.navigate(['/']); // Se non ha il ruolo, torna in home
      return false;
    }
    return true;
  }

  // Se non è loggato, avvia il login
  authService.login();
  return false;
};
