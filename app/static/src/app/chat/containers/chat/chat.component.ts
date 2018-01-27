import { Component } from "@angular/core";

@Component({
  selector: 'chat',
  template: `
    <div class="chat">
      <div class="message-wrapper">
        <div class="message-container">
          <div class="message-list">
            <div class="message-item message-item-right" *ngFor="let message of messages">
              {{ message }}
            </div>
          </div>
        </div>
      </div>
      <div class="send-box">
        <div class="input-group">
          <input type="text" class="form-control" placeholder="" aria-label="" aria-describedby="basic-addon1">
          <div class="input-group-prepend">
            <button class="btn btn-outline-secondary" type="button">Submit</button>
          </div>
        </div>
      </div>
    </div>
  `,
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent {
  messages = ['afewafea', 'fewafewafewa', 'fewafewafewa']
}
