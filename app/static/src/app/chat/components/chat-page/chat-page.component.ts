import { Component } from '@angular/core';

@Component({
  selector: 'chat-page',
  template: `
    <div class="chat-box">
      <div class="text-center">
        <h1>Chat</h1>
      </div>
      <chat class="chat"></chat>
    </div>
  `,
  styleUrls: ['./chat-page.component.scss']
})
export class ChatPageComponent {

}
