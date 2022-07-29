$('document').ready(function(){
    
    checkCart();
    showCart();

  
   $('#sub_button').on('click',addToBase);
});

function showCart(){
        if($.isEmptyObject(cart)){
            $('#cart').html('Cart is empty');
            $('#sub_button').prop('disabled', true);
        }else{
        var out='';
        var oneGood={};
        var newdata={};
        var total_price=0;    
        
        for(var k1 in data){
            var a = data[k1]['pk'];
            var b = data[k1]['fields'];
            newdata[a] ={
            'name': b['title'],
            'cost': b['price'],
            'image': b['img']
           }
           
        }

        for(var str_id in cart){
            var key = str_id.split(':');
            
            oneGood=newdata[key[1]];
            total_price+=oneGood.cost*cart[str_id];
           
                out+= '<div class="row p-3">';
                out+= '  <div class="col">';
                out+= '     <img class="img-thumbnail float-left d-inline-flex p-2" src="/media/'+oneGood.image+'" width="200px">';
                out+= '  </div>';
                out+= '  <div class="col-4 p-4">';
                out+= '      <h2>'+oneGood.name+'</h2>';
                out+= '      <p>'+oneGood.cost+' грн. * '+cart[str_id]+' = '+oneGood.cost*cart[str_id]+' грн.</p>';
                
                out+= '   <button type="button" class="btn btn-outline-success btn-sm plusGoods" data-id="'+key[0]+':'+key[1]+'">+</button>';
                out+= '   <button type="button" class="btn btn-outline-success btn-sm minusGoods" data-id="'+key[0]+':'+key[1]+'">-</button>';
                out+= '   <button type="button" class="btn btn-outline-danger btn-sm deleteGoods" data-id="'+key[0]+':'+key[1]+'">X</button>';
                out+= '   </div>';
                out+= '</div>';
              
        }
        $('#cart').html(out);
        $('#total_price').html(total_price);   
        $('button.plusGoods').on('click',plusGoods);
        $('button.minusGoods').on('click',minusGoods);
        $('button.deleteGoods').on('click',deleteGoods);
        
    }
}
    
function plusGoods(){
        var id_goods = $(this).attr('data-id');
        cart[id_goods]++;
        localStorage.setItem('cart',JSON.stringify(cart));
        showCart();
    }
function minusGoods(){
        var id_goods = $(this).attr('data-id');
        if(cart[id_goods]!=1){
        cart[id_goods]--;
        localStorage.setItem('cart',JSON.stringify(cart));
        showCart();
        }
    }
function deleteGoods(){
        var id_goods = $(this).attr('data-id');
        
        delete cart[id_goods];
        localStorage.setItem('cart',JSON.stringify(cart));
        showCart();
        
    }
    
function addToBase(){
        var userdata={};
        var oneGood='';
        var total_price=0;
        var userOrder={};
        var out_string='';
        var out_goods='';
        var c=0;

        var flag_form = false;
        var email = document.getElementById('form_email').value;
        var name = document.getElementById('form_name').value;
        var phone = document.getElementById('form_phone').value;
        var adress = document.getElementById('form_adress').value;

        if ((email!='')&&(name!='')&&(phone!='')&&(adress!=''))flag_form=true;
      
       // console.log(flag_form);
        if(flag_form){

                out_string+= '<div class="row">';
                out_string+= '  <div class="p-4">';
                out_string+= '      <h1>Your Order Cart</h1>';              
                console.log(cart);
                for(var str_id in cart){
                    var key = str_id.split(':');
                    oneGood=data[key[0]]['goods'][key[1]];
            
                    total_price+=oneGood.cost*cart[str_id];
                    userOrder[c]={
                        'name': oneGood.name,
                        'cost': oneGood.cost,
                        'count': cart[str_id],
                        'summa': oneGood.cost*cart[str_id]
                    };  
                    c++;
                    out_goods+='<p><b>'+c+'</b> '+oneGood.name+' '+oneGood.cost+' РіСЂРЅ. * '+cart[str_id]+' = '+oneGood.cost*cart[str_id]+' РіСЂРЅ.</p>'; 
                    }
           
                    userdata[email]={
                            'name': name,
                            'phone' : phone,
                            'adress' : adress,
                            'cart' : userOrder,
                            'totalprice' : total_price
                            };
                out_string+= '<p><b>Name:</b> '+name+'</p>';
                out_string+= '<p><b>Email:</b> '+email+'</p>'; 
                out_string+= '<p><b>Phone:</b> '+phone+'</p>';
                out_string+= '<p><b>Adress:</b> '+adress+'</p>';
                out_string+= '<p></p>';
                out_string+= '<hr>';
                out_string+= out_goods;
                out_string+= '<hr>';
                out_string+= '<div class="row"><div class="col-4"><b>Total price:</b></div><div class="col-4"> <b>'+total_price+' РіСЂРЅ.</b></div></div>';            
                                      
                out_string+= '   </div>';
                out_string+= '</div>';

                localStorage.setItem('userdata',JSON.stringify(userdata));
    
                cart={};
                localStorage.setItem('cart',JSON.stringify(cart));
                

                $('#modal_text').html(out_string);
                $('#myModal').modal('show');
                $('#myModal').on('hidden.bs.modal', function (e) {
                    document.getElementById('form').submit();
                  });
                
                
            }else{
                $('#hinddenBtn').trigger("click");
                
            }
            
    };




function checkCart(){
    if(localStorage.getItem('cart')!=null){
        cart= JSON.parse(localStorage.getItem('cart'));
    }
}


