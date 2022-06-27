export const actions = {
  activePopup() {
    let popup = document.querySelector('.popup-section');
    popup.classList.add('active');
  },
  closePopup() {
    let popup = document.querySelector('.popup-section');
    popup.classList.remove('active');
  },

  editPopup() {
    this.activePopup();
  },
};
