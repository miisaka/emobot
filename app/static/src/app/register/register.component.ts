import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  username: String;
  password: String;
  contactName: String;
  contactNumber: String;
  relationshipToContact: String;
  elderly: Boolean;
  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  onRegisterSubmit() {
    const user = {
      username: this.username,
      password: this.password,
      contactName: this.contactName,
      contactNumber: this.contactNumber,
      relationshipToContact: this.relationshipToContact,
      elderly: this.elderly
    }
    this.http.post('http://localhost:4200/api/register', user).subscribe(data => {
      console.log(data);
    });
  }

}
