import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';  // <-- #1 import module
import { HttpClientModule } from '@angular/common/http';

// chat
import { ChatModule } from "./chat/chat.module";
import { ChatPageComponent } from "./chat/components/chat-page/chat-page.component";

const ROUTES: Routes = [
  { path: '', pathMatch: 'full', component: ChatPageComponent },
  { path: 'login', pathMatch: 'full', component: LoginComponent},
  { path: 'register', pathMatch: 'full', component: RegisterComponent}

];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    RegisterComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    ChatModule,
    RouterModule.forRoot(ROUTES),
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule{}
