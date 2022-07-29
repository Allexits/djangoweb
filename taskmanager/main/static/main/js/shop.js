$('document').ready(function(){
    checkCart();
    
    $('button.add-to-cart').on('click',addToCart); 
});

function addToCart(){
    if(typeof cart == "undefined"){
        cart={}
    }
    
    var id_goods = $(this).attr('data-id');
    if(cart[id_goods]!=undefined){
        cart[id_goods]++;
    }
    else 
        cart[id_goods]=1;

    localStorage.setItem('cart',JSON.stringify(cart));
    
    $('#myModal').modal('show')
}

function checkCart(){
    if(localStorage.getItem('cart')!=null){
        cart= JSON.parse(localStorage.getItem('cart'));
    }
}