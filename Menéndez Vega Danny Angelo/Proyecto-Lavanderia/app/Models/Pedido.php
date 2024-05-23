<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Pedido extends Model
{
    use HasFactory;
    protected $table = 'pedidos';
    protected $primaryKey = 'id_pedido';
    protected $fillable = ['id_cliente', 'id_metodo_pago', 'cantidad_pedido', 'fecha_pedido','observacion'];

    public function cliente()
    {
        return $this->belongsTo(Cliente::class, 'id_cliente', 'id_cliente');
    }

    public function metodoPago()
    {
        return $this->belongsTo(MetodoPago::class, 'id_metodo_pago', 'id_metodo_pago');
    }

    public function pedidoServicios()
    {
        return $this->hasMany(PedidoServicio::class, 'id_pedido', 'id_pedido');
    }
}
