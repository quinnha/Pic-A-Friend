package com.google.ar.core.examples.java.common.samplerender;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.FloatBuffer;
import java.nio.IntBuffer;

import de.javagl.obj.Obj;
import de.javagl.obj.ObjData;
import de.javagl.obj.ObjReader;
import de.javagl.obj.ObjUtils;

public class MeshUtil {

    /**
     * Constructs a {@link Mesh} from the given Wavefront OBJ file.
     *
     * <p>The {@link Mesh} will be constructed with three attributes, indexed in the order of local
     * coordinates (location 0, vec3), texture coordinates (location 1, vec2), and vertex normals
     * (location 2, vec3).
     */
    public static Mesh createFromObj(SampleRender render, String objStr) throws IOException {
        InputStream inputStream = new ByteArrayInputStream(objStr.getBytes());
        Obj obj = ObjUtils.convertToRenderable(ObjReader.read(inputStream));

        // Obtain the data from the OBJ, as direct buffers:
        IntBuffer vertexIndices = ObjData.getFaceVertexIndices(obj, /*numVerticesPerFace=*/ 3);
        FloatBuffer localCoordinates = ObjData.getVertices(obj);
        FloatBuffer textureCoordinates = ObjData.getTexCoords(obj, /*dimensions=*/ 2);
        FloatBuffer normals = ObjData.getNormals(obj);

        VertexBuffer[] vertexBuffers = {
                new VertexBuffer(render, 3, localCoordinates),
                new VertexBuffer(render, 2, textureCoordinates),
                new VertexBuffer(render, 3, normals),
        };

        IndexBuffer indexBuffer = new IndexBuffer(render, vertexIndices);

        return new Mesh(render, Mesh.PrimitiveMode.TRIANGLES, indexBuffer, vertexBuffers);
    }
}
