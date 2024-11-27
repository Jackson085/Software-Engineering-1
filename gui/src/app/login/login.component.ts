import { Component, computed } from '@angular/core';
import { signal } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  email = signal<string>('');
  password = signal<string>('');
  isEmailBlur = signal<boolean>(false)
  hasLoginAttempted = signal<boolean>(false);
  isLoginValid = signal<boolean>(false)
  
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
    this.email.set(input.value);
  }
}

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;