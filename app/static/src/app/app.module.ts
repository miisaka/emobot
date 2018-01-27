import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { RouterModule, Routes } from "@angular/router";

// chat
import { ChatModule } from "./chat/chat.module";
import { ChatPageComponent } from "./chat/components/chat-page/chat-page.component";
import { RegisterComponent } from './register/register.component';

const ROUTES: Routes = [
  { path: '', pathMatch: 'full', component: ChatPageComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    RegisterComponent,
  ],
  imports: [
    BrowserModule,
    ChatModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
