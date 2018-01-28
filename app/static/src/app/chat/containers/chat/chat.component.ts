import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import { HttpClient } from "@angular/common/http";
import {Router} from '@angular/router';


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
        <div class="message-container" #messageContainer>
          <div class="message-list" #messageList>
            <div class="message-item" [ngClass]="'message-item-' + (message.isRight ? 'right' : 'left')" *ngFor="let message of messages">
              {{ message.body }}
            </div>
          </div>
        </div>
      </div>
      <div class="chat-action" [class.chat-action-typing]="loading">
        Harold is replying...
      </div>
      <div class="send-box">
        <form [formGroup]="form" (submit)="submitMessage($event)">
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
export class ChatComponent implements OnInit {

  @ViewChild('messageContainer')
  messageContainer: ElementRef;

  @ViewChild('messageList')
  messageList: ElementRef;

  loading = false;

  messages: Message[] = [ ];

  form = new FormGroup({
    message: new FormControl('', Validators.required)
  });

  constructor(
    private http: HttpClient,
    private router: Router
  ) { }

  ngOnInit() {
    this.http.post('http://localhost:4200/api/chat', { message: 'welcome' })
      .subscribe((res: any) => {
        this.messages.push({
          isRight: false,
          body: res.message
        });
      })
  }

  submitMessage($event) {
    $event.preventDefault();

    if (this.form.valid) {

      this.loading = true;

      this.http.post('http://localhost:4200/api/chat', this.form.value)
        .catch((err) => Observable.throw(err))
        .subscribe((res: any) => {

          this.addNewMessage(true, this.form.value.message);
          this.addNewMessage(false, res.message);

          this.scrollChat();
          this.form.reset();
          this.loading = false;

        }, (err) => {
          this.loading = false;
      });
    }
  }

  scrollChat() {
    setTimeout(() => {
      this.messageContainer.nativeElement.scrollTop = this.messageList.nativeElement.clientHeight;
    });
  }

  addNewMessage(isRight: boolean, message: string) {
    this.messages.push({ isRight, body: message });
  }

}
