import { Component } from '@angular/core';
import {Character} from '../character';

@Component({
  selector: 'app-characters',
  standalone: true,
  imports: [],
  templateUrl: './characters.component.html',
  styleUrl: './characters.component.css'
})
export class CharactersComponent {
  character: Character = {
    id: 1,
    name: 'Kafka'
  }
}
