let updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener("click", function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        let user = this.dataset.user;
        console.log("Product ID: " + productId + "\nAction: " + action);

        console.log("USER:", user);
    })
}