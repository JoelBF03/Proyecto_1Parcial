<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TipoServicio extends Model
{
    use HasFactory;
    protected $table = 'tipo_servicio';
    protected $primaryKey = 'id_tipo_servicio';
    protected $fillable = ['nombre','descripcion'];

    public function pedidosServicios()
    {
        return $this->hasMany(PedidoServicio::class, 'id_tipo_servicio', 'id_tipo_servicio');
    }
}
