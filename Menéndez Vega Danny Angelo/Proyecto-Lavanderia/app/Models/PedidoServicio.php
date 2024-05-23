<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class PedidoServicio extends Model
{
    use HasFactory;

    protected $table = 'pedido_servicio';
    protected $primaryKey = 'id';
    protected $fillable = ['id_pedido', 'id_tipo_servicio', 'cantidad_servicio', 'descripcion'];

    public function pedido()
    {
        return $this->belongsTo(Pedido::class, 'id_pedido', 'id_pedido');
    }

    public function tipoServicio()
    {
        return $this->belongsTo(TipoServicio::class, 'id_tipo_servicio', 'id_tipo_servicio');
    }
}
