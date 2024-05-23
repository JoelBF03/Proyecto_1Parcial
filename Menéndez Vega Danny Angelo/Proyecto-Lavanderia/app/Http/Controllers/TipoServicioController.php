<?php

namespace App\Http\Controllers;

use App\Models\TipoServicio;
use Illuminate\Http\Request;

class TipoServicioController extends Controller
{

    public function index()
    {
        $tipos_servicio = TipoServicio::withCount('pedidosServicios')->get();

        return response()->json($tipos_servicio);
    }

    public function store(Request $request)
    {
        $request->validate([
            'descripcion' => 'required',
        ],[
            'descripcion.required' => 'La descripción es requerida',]);

        $tipo_servicio = TipoServicio::create($request->all());
        return response()->json($tipo_servicio);
    }
    public function show($id)
    {
        $tipo_servicio = TipoServicio::find($id);
        return response()->json($tipo_servicio);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'descripcion' => 'required',
        ],[
            'descripcion.required' => 'La descripción es requerida',]);
        $tipo_servicio = TipoServicio::find($id);
        $tipo_servicio->update($request->all());
        return response()->json($tipo_servicio);
    }

    public function destroy($id)
    {
        $tipo_servicio = TipoServicio::find($id);
        $tipo_servicio->update(['activo' => false]);
        return response()->json(null, 204);
    }
}
