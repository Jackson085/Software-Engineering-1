import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { User } from '../models/user.type';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private readonly loginUrl = 'http://127.0.0.1:5000/login';

  constructor(private http: HttpClient) { }

  /**
   * Logs in a user with email and password.
   *
   * @param {string} email - The user's email.
   * @param {string} password - The user's password.
   * @returns {Observable<User>} An observable that resolves to a User object.
   */
  login(email: string, password: string): Observable<User> {
    const payload = {email, password};
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    return this.http.post<{token: string}>(this.loginUrl, payload, {headers}).pipe(
      map((response) => {
        return {
          username: email,
          email: email,
          token: response.token
        } as User;
      }),
      catchError(this.handleError)
    )
  }

  /**
   * Handles HTTP errors.
   *
   * @param {HttpErrorResponse} error - The HTTP error response.
   * @returns {Observable<never>} An observable error.
   */
  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An unknown error occurred';
    if (error.error instanceof ErrorEvent) {
      // Client-side or network error
      errorMessage = `Client-side error: ${error.error.message}`;
    } else {
      // Server-side error
      if (error.status === 401) {
        errorMessage = 'Invalid username or password';
      } else if (error.error && error.error.message) {
        errorMessage = `Server error: ${error.error.message}`;
      } else {
        errorMessage = `Server returned code ${error.status}`;
      }
    }
    return throwError(() => new Error(errorMessage));
  }
}
