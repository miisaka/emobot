import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {FormBuilder, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  form = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required],
    contactName: ['', Validators.required],
    contactNumber: ['', Validators.required],
    relationshipToContact: ['', Validators.required],
    elderly: ['', Validators.required],
  });

  constructor(
    private http: HttpClient,
    private fb: FormBuilder,
    private router: Router,
    private toastr: ToastrService
  ) { }

  ngOnInit() {
  }

  onRegisterSubmit($event) {
    $event.preventDefault();

    console.log(this.form.value);

    if (this.form.valid && this.form.value.elderly) {
      this.http.post('http://localhost:4200/api/register', this.form.value).subscribe(data => {
        this.router.navigate(['/login']);
      }, (err) => {
        console.log(err);
      });
    }

  }

}
