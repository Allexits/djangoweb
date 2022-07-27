var cart={};

$('document').ready(function(){

    loadShops();
    loadGoods();
    checkCart();
   
})
function loadShops(){
    $.getJSON('goods.json',function(data){
        
        var out = '';
        for(var item in data){
            out+= '<li class="nav-item">';
            out+= '<img src="'+data[item]['image']+'" alt="Bootstrap" width="42" height="42">';
            out+= '<button class="btn btn-lg btn-block shop " data-id="'+item+'">';                  
            out+= data[item]['name'];
            out+= '</button></li></br>';
        }
        $('#shops').html(out);
        $('.shop').on('click',loadGoodsShop);
    });
}
function loadGoodsShop(){
    var id = $(this).attr('data-id');
    loadGoods(id);

}

function loadGoods(id=1){
    $.getJSON('goods.json',function(data){
        var out = '';
            var goods =  data[id]['goods'];
            for(var key in goods){
                out+= '<div class="col">';
                out+= '<div class="card shadow-sm">';
                out+= '  <img class="img-thumbnail" src="'+goods[key]['image']+'">';
                out+= '  <div class="card-body">';
                out+= '  <div class="d-flex justify-content-between">';
                out+= '     <h5 class="card-title">'+goods[key]['name']+'</h5>';
                out+= '     <div class="bd-highlight">'+goods[key]['cost']+' РіСЂРЅ.</div>';
                out+= '</div>';
                out+= '    <div class="d-flex justify-content-end">';
                out+= '      <div class="btn-group">';
                out+= '        <button type="button" class="btn btn-sm btn-outline-secondary add-to-cart" data-id="'+[id]+':'+[key]+'">Add to Cart</button>';
                out+= '      </div>';
                out+= '    </div>';
                out+= '  </div>';
                out+= '</div>';
                out+= '</div>';
            }
        $('#goods').html(out);
        $('button.add-to-cart').on('click',addToCart);
        
    });
}
function addToCart(){
    var id_goods = $(this).attr('data-id');
    if(cart[id_goods]!=undefined){
        cart[id_goods]++;
    }
    else 
        cart[id_goods]=1;

    localStorage.setItem('cart',JSON.stringify(cart));
    checkCart();
    $('#myModal').modal('show')
}

function checkCart(){
    if(localStorage.getItem('cart')!=null){
        cart= JSON.parse(localStorage.getItem('cart'));
    }
}