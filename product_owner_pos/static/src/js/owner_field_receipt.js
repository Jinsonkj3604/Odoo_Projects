odoo.define('product_owner_pos.receipt', function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_fields('product.product', 'owner_id');

var _super_orderline = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    export_for_printing: function() {
        var line = _super_orderline.export_for_printing.apply(this,arguments);
        line.owner_id = this.get_product().owner_id;
        return line;
    },
});

});