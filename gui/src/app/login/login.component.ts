import { Component, computed } from '@angular/core';
import { signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  constructor(private router: Router) {}

  email = signal<string>('');
  password = signal<string>('');
  isEmailBlur = signal<boolean>(false);
  hasLoginAttempted = signal<boolean>(false);
  isLoginValid = signal<boolean>(false);
  
  isEmailValid = computed(() => EMAIL_REGEX.test(this.email()))

  onEmailInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.email.set(input.value);
  }

  onEmailBlur(): void {
    this.isEmailBlur.set(true);
  }

  onPasswordInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.password.set(input.value);
  }

  onLogin(): void {
    const isLoginValid: boolean = false;
    if (isLoginValid) {
      this.isLoginValid.set(true);
      this.hasLoginAttempted.set(true);
      this.router.navigate(['/'])
    } else {
      this.isLoginValid.set(false);
      this.hasLoginAttempted.set(true);
    }
  }

  onRegister(): void {
    this.router.navigate(['/register']);
  }

  onLegalInfo(): void {
    this.router.navigate(['/legal']);
  }
}

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;