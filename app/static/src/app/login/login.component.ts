import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import {FormBuilder, Validators} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

   form = this.fb.group({
     username: ['', Validators.required],
     password: ['', Validators.required],
   });
  constructor(private http: HttpClient,
              private fb: FormBuilder,
              private router: Router) { }
  ngOnInit() {
  }

  onLoginSubmit($event) {
     $event.preventDefault();
     console.log(this.form.value);

    if (this.form.valid) {
      this.http.post('http://localhost:4200/api/login', this.form.value).subscribe(data => {
        this.router.navigate(['/']);
      }, (err) => {
        console.log(err);
      });
    } else {
      this.router.navigate(['/login']);
    }
  }

}
