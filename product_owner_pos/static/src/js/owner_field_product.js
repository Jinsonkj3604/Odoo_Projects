odoo.define('product_owner_pos.product', function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_fields('product.product', 'owner_id');

var _super_orderline = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    initialize: function() {
        var line = _super_orderline.initialize.apply(this,arguments);
        this.owner_id = this.get_product().owner_id;
        return line;
    },
});

});