import { NgModule } from '@angular/core';
import { CommonModule } from "@angular/common";

// components
import { ChatPageComponent } from "./components/chat-page/chat-page.component";

// container
import { ChatComponent } from "./containers/chat/chat.component";

@NgModule({
  declarations: [
    ChatPageComponent,
    ChatComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    ChatPageComponent
  ]
})
export class ChatModule { }
