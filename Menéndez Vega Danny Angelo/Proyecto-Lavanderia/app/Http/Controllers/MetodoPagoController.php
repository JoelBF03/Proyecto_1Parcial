<?php

namespace App\Http\Controllers;

use App\Models\MetodoPago;
use Illuminate\Http\Request;

class MetodoPagoController extends Controller
{

    public function index()
    {
        $metodos_pago = MetodoPago::all();
        return response()->json($metodos_pago);
    }

    public function store(Request $request)
    {
        $request->validate([
            'nombre' => 'required',
            'descripcion' => 'required',
        ],[
            'nombre.required' => 'El nombre es requerido',
            'descripcion.required' => 'La descripción es requerida',]);

        $metodo_pago = MetodoPago::create($request->all());
        return response()->json($metodo_pago);
    }

    public function show($id)
    {
        $metodo_pago = MetodoPago::find($id);
        return response()->json($metodo_pago);
    }
    public function update(Request $request, $id)
    {
        $request->validate([
            'nombre' => 'required',
            'descripcion' => 'required',
        ],[
            'nombre.required' => 'El nombre es requerido',
            'descripcion.required' => 'La descripción es requerida',]);
        $metodo_pago = MetodoPago::find($id);
        $metodo_pago->update($request->all());
        return response()->json($metodo_pago);
    }
    public function destroy($id)
    {
        $metodo_pago = MetodoPago::find($id);
        $metodo_pago->update(['activo' => false]);
        return response()->json(null, 204);
    }
}
