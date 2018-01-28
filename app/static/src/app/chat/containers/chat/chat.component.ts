import { Component } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import { HttpClient } from "@angular/common/http";


import 'rxjs/add/operator/catch';
import { Observable } from "rxjs/Observable";

export interface Message {
  isRight: boolean;
  body: string;
}

@Component({
  selector: 'chat',
  template: `
    <div class="chat">
      <div class="message-wrapper">
        <div class="message-container">
          <div class="message-list">
            <div class="message-item" [ngClass]="'message-item-' + (message.isRight ? 'right' : 'left')" *ngFor="let message of messages">
              {{ message.body }}
            </div>
          </div>
        </div>
      </div>
      <div class="send-box">
        <form [formGroup]="form" (submit)="submitMessage()">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="Type a message!" aria-label="" aria-describedby="basic-addon1" formControlName="message" autofocus>
            <div class="input-group-prepend">
              <button class="btn btn-outline-secondary" type="button" value="Submit">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  `,
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent {

  messages: Message[] = [
    { isRight: false, body: 'Hello ' + 'user' + ', how are you today?' },
    { isRight: true, body: 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH' },
    { isRight: false, body: 'lorafewafewa' },
    { isRight: false, body: 'lorafewafewa' },
  ];

  form = new FormGroup({
    message: new FormControl('', Validators.required)
  });

  constructor(
    private http: HttpClient
  ) { }

  submitMessage() {
    console.log(this.form.value);
    if (this.form.valid) {
      this.http.post('http://localhost:4200/api/chat', this.form.value)
        .catch((err) => Observable.throw(err))
        .subscribe((res) => {
        }, (err) => {

      });
    }
  }

}
