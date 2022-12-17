odoo.define('session_wise_discount_pos.ProductScreen', function (require) {
    'use strict';

    const {Gui} = require('point_of_sale.Gui');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');
    var discount_total= 0;

    const SessionDiscountLimitPOS = (ProductScreen) =>
        class extends ProductScreen {
            async _onClickPay() {

            console.log(this,"PAYMENT CLICKED")
            var pos = this.env.pos;
            var limit = pos.config.maxim_discount;
            var category = pos.config.catg_id;
            var session_id = pos.pos_session.id
            var track1 = [['session_id', '=', session_id]]
            var all_orders = [];
            var order_line_id = [];
            var product_id = [];
            var pre_discount = 0;

            await rpc.query({
                model: 'pos.order',
                method: 'search_read',
                args: [track1]
            }).then(function(result){
            console.log(result,"Session Orders")
                result.forEach(function(object){
                    all_orders.push(object['id'])
                })
            });
            var track2 = [['order_id', '=', all_orders]]
             await rpc.query({
                model: 'pos.order.line',
                method: 'search_read',
                args: [track2]
            }).then(function(result){
            console.log(result,"order lines in the session")
                result.forEach(function(object){
                    order_line_id.push(object)
                })
            });
            order_line_id.forEach(function(i){
                product_id.push(i.product_id[0])
            })

            var track3 = [['id', 'in', product_id]]
             await rpc.query({
                model: 'product.product',
                method: 'search_read',
                args: [track3]
            }).then(function(result){
            console.log(result,"Product")
                result.forEach(function(object){
                if (category[0] == object.pos_categ_id[0]){
                    order_line_id.forEach(function(line){
                    if (object.id == line.product_id[0]){
                    var discount_amount = ((line.price_unit * (line.discount / 100)) * line.qty)
                    pre_discount = discount_amount + pre_discount
                    }
                    })
                    console.log(pre_discount,"preview")
                }
                })
            });
            console.log("this",this)
            var current_discount = this.currentOrder.orderlines.models
                current_discount.forEach(function(obj){
                if (category[0] == obj.product.pos_categ_id[0]){
                    var this_discount_amount = ((obj.price * (obj.discount / 100)) * obj.quantity)
                    discount_total = pre_discount + this_discount_amount

                }

                })
                console.log(discount_total)
                if (discount_total > limit){
                        Gui.showPopup('ErrorPopup',{
                        'title': ('Session Discount'),
                        'body': ('Discount limit Exceeded !!')
                        });
                }
                else{
                        await super._onClickPay()
                }
            }
        };

    Registries.Component.extend(ProductScreen, SessionDiscountLimitPOS);
    return ProductScreen;
});

