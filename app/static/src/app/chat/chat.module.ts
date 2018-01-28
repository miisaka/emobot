import { NgModule } from '@angular/core';
import { CommonModule } from "@angular/common";
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";

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
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  exports: [
    ChatPageComponent
  ]
})
export class ChatModule { }
