import { Component, computed } from '@angular/core';
import { signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  constructor(
    private router: Router,
    private loginService: LoginService
  ) {}

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
    console.log(this.email(), this.password())
    if (this.isEmailValid() && this.password()) {
      this.loginService.login(this.email(), this.password()).subscribe({
        next: (user) => {
          // Store token in localStorage
          localStorage.setItem('token', user.token);

          // Update login state
          this.isLoginValid.set(true);
          this.hasLoginAttempted.set(true);

          // Redirect to the home page
          this.router.navigate(['/home']);
        },
        error: (err) => {
          console.error('Login failed:', err);
          this.isLoginValid.set(false);
          this.hasLoginAttempted.set(true);
        }
      });
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