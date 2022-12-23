/** @odoo-module*/

odoo.define('website_quotation_confirmation.CheckBoxAction', function (require) {
    "use strict";
    console.log("worked")

    var ajax = require('web.ajax');
    var order_list=[];

    $('.checkbox-cls').change(function(){
    console.log(131314)
    if($(this).is(':checked')){
        console.log(this.value)
        order_list.push(this.value)
        console.log(order_list)
    }
    $('#order_confirm').on('click', function(){
        console.log("111")
        ajax.jsonRpc('/checkbox/active/order','call', {'data': order_list})
    })
    })
    })