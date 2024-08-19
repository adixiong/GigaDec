class Menu {
  static #menu = $("#menu");
  static #horizontalMenu = $("#horizontal-menu");

  static open() {
    this.#menu.slideToggle(300);
    this.#horizontalMenu.hide();
  }

  static hide() {
    this.#menu.slideToggle(300,()=>{
        this.#horizontalMenu.fadeIn();
    })
  }
}

// Close Menu Btn handler
$("#close-menu-btn").click(() => Menu.hide());

// Open Menu Btn handler
$("#open-menu-btn").click(() => Menu.open());

