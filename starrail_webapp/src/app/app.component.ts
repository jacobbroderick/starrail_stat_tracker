import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CharactersComponent } from './characters/characters.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CharactersComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'starrail tracker';
}
