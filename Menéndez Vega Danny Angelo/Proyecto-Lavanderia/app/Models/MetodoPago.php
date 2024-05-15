<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MetodoPago extends Model
{
    use HasFactory;
    protected $table = 'metodo_pago';
    protected $primaryKey = 'id_metodo_pago';
    protected $fillable = ['description'];

    public function pedidos()
    {
        return $this->hasMany(Pedido::class, 'id_metodo_pago', 'id_metodo_pago');
    }
}
