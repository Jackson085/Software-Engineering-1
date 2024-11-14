import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-galerie',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './galerie.component.html',
  styleUrls: ['./galerie.component.scss']
})
export class GalerieComponent {
  images = [
    { title: 'Bild 1' },
    { title: 'Bild 2' },
    { title: 'Bild 3' }
  ];

  addImage() {
    const newImage = { title: 'Neues Bild' };
    this.images.push(newImage);
  }

  deleteImage(index: number) {
    this.images.splice(index, 1);
  }

  editImage(index: number) {
    const newTitle = prompt('Neuen Titel für das Bild eingeben:', this.images[index].title);
    if (newTitle !== null && newTitle !== '') {
      this.images[index].title = newTitle;
    }
  }
}
